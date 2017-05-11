using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using LinearMachineLearning.DataHandling;
using MathNet.Numerics.LinearAlgebra;

namespace LinearMachineLearning.LearningAlgorithms
{
    public class LinearRegression : LinearModel
    {
        #region Parameters
        #endregion

        #region Constructors
        public LinearRegression()
        {

        }
        public LinearRegression(int inputSize)
        {
            InputSize = inputSize;
            Inputs = new double[InputSize];
            Weights = new double[InputSize];
            Output = 0;
            InSampleError = 0;
        }
        public LinearRegression(string filePath)
        {
            FilePath = filePath;
            string[] lines = System.IO.File.ReadAllLines(filePath);

            Name = lines[0];
            InputSize = Convert.ToInt32(lines[1]);
            Inputs = new double[InputSize];
            Weights = new double[InputSize];

            string[] stringWeights = lines[2].Split(',');
            for (int index = 0; index < stringWeights.Length; index++)
            {
                Weights[index] = Convert.ToDouble(stringWeights[index]);
            }

            InSampleError = 0;
            Output = 0;
        }
        #endregion

        #region Methods
        public override void Learn(DataSet set)
        {
            Matrix<double> inMatrix = GetMatrixFromInputs(set);
            Vector<double> desiredOutVector = GetVectorFromDesiredOutputs(set);

            Vector<double> result = (inMatrix.PseudoInverse()).Multiply(desiredOutVector);
            Weights = result.ToArray();
        }
        public override void ComputeInSampleError(DataSet set)
        {
            InSampleError = 0;
            foreach (DataPoint point in set.Examples)
            {
                InSampleError += ComputeSinglePointError(point);
            }
            InSampleError /= set.NumberExamples;
        }
        public override double ComputeSinglePointError(DataPoint point)
        {
            ComputeOutput(point.Input);
            return Math.Pow(Output - point.Output, 2);
        }
        public Matrix<double> GetMatrixFromInputs(DataSet set)
        {
            List<double[]> inputs = new List<double[]>();
            foreach (DataPoint point in set.Examples)
            {
                inputs.Add(point.Input);
            }
            Matrix<double> matrix = CreateMatrix.DenseOfRowArrays(inputs);

            return matrix;
        }
        public Vector<double> GetVectorFromDesiredOutputs(DataSet set)
        {
            List<double> des = new List<double>();
            foreach(DataPoint point in set.Examples)
            {
                des.Add(point.Output);
            }
            return CreateVector.DenseOfEnumerable(des);
        }
        #endregion
    }
}
